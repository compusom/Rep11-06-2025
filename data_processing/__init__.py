"""Data processing utilities for the report generator project.

This package groups modules for loading raw data, aggregating statistics,
calculating metrics and orchestrating the creation of formatted reports.
"""

from .orchestrators import procesar_reporte_rendimiento, procesar_reporte_bitacora
__all__ = ["procesar_reporte_rendimiento", "procesar_reporte_bitacora"]
