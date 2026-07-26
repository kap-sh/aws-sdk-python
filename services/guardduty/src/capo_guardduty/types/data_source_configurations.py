"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSourceConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.kubernetes_configuration
    import capo_guardduty.types.malware_protection_configuration
    import capo_guardduty.types.s3_logs_configuration


class DataSourceConfigurations(TypedDict, closed=True):
    s3_logs: NotRequired[
        "capo_guardduty.types.s3_logs_configuration.S3LogsConfiguration"
    ]
    """<p>Describes whether S3 data event logs are enabled as a data source.</p>"""
    kubernetes: NotRequired[
        "capo_guardduty.types.kubernetes_configuration.KubernetesConfiguration"
    ]
    """<p>Describes whether any Kubernetes logs are enabled as data sources.</p>"""
    malware_protection: NotRequired[
        "capo_guardduty.types.malware_protection_configuration.MalwareProtectionConfiguration"
    ]
    """<p>Describes whether Malware Protection is enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfigurations) -> dict:
    out: dict = {}
    if "s3_logs" in value:
        import capo_guardduty.types.s3_logs_configuration

        out["s3Logs"] = capo_guardduty.types.s3_logs_configuration.serialize_json(
            value["s3_logs"]
        )
    if "kubernetes" in value:
        import capo_guardduty.types.kubernetes_configuration

        out["kubernetes"] = (
            capo_guardduty.types.kubernetes_configuration.serialize_json(
                value["kubernetes"]
            )
        )
    if "malware_protection" in value:
        import capo_guardduty.types.malware_protection_configuration

        out["malwareProtection"] = (
            capo_guardduty.types.malware_protection_configuration.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceConfigurations:
    out: DataSourceConfigurations = {}  # type: ignore[typeddict-item]
    if "s3Logs" in data:
        import capo_guardduty.types.s3_logs_configuration

        out["s3_logs"] = capo_guardduty.types.s3_logs_configuration.deserialize_json(
            data["s3Logs"]
        )
    if "kubernetes" in data:
        import capo_guardduty.types.kubernetes_configuration

        out["kubernetes"] = (
            capo_guardduty.types.kubernetes_configuration.deserialize_json(
                data["kubernetes"]
            )
        )
    if "malwareProtection" in data:
        import capo_guardduty.types.malware_protection_configuration

        out["malware_protection"] = (
            capo_guardduty.types.malware_protection_configuration.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
