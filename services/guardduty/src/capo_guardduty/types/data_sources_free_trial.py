"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSourcesFreeTrial``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.data_source_free_trial
    import capo_guardduty.types.kubernetes_data_source_free_trial
    import capo_guardduty.types.malware_protection_data_source_free_trial


class DataSourcesFreeTrial(TypedDict, closed=True):
    cloud_trail: NotRequired[
        "capo_guardduty.types.data_source_free_trial.DataSourceFreeTrial"
    ]
    """<p>Describes whether any Amazon Web Services CloudTrail management event logs are enabled as data sources.</p>"""
    dns_logs: NotRequired[
        "capo_guardduty.types.data_source_free_trial.DataSourceFreeTrial"
    ]
    """<p>Describes whether any DNS logs are enabled as data sources.</p>"""
    flow_logs: NotRequired[
        "capo_guardduty.types.data_source_free_trial.DataSourceFreeTrial"
    ]
    """<p>Describes whether any VPC Flow logs are enabled as data sources.</p>"""
    s3_logs: NotRequired[
        "capo_guardduty.types.data_source_free_trial.DataSourceFreeTrial"
    ]
    """<p>Describes whether any S3 data event logs are enabled as data sources.</p>"""
    kubernetes: NotRequired[
        "capo_guardduty.types.kubernetes_data_source_free_trial.KubernetesDataSourceFreeTrial"
    ]
    """<p>Describes whether any Kubernetes logs are enabled as data sources.</p>"""
    malware_protection: NotRequired[
        "capo_guardduty.types.malware_protection_data_source_free_trial.MalwareProtectionDataSourceFreeTrial"
    ]
    """<p>Describes whether Malware Protection is enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourcesFreeTrial) -> dict:
    out: dict = {}
    if "cloud_trail" in value:
        import capo_guardduty.types.data_source_free_trial

        out["cloudTrail"] = capo_guardduty.types.data_source_free_trial.serialize_json(
            value["cloud_trail"]
        )
    if "dns_logs" in value:
        import capo_guardduty.types.data_source_free_trial

        out["dnsLogs"] = capo_guardduty.types.data_source_free_trial.serialize_json(
            value["dns_logs"]
        )
    if "flow_logs" in value:
        import capo_guardduty.types.data_source_free_trial

        out["flowLogs"] = capo_guardduty.types.data_source_free_trial.serialize_json(
            value["flow_logs"]
        )
    if "s3_logs" in value:
        import capo_guardduty.types.data_source_free_trial

        out["s3Logs"] = capo_guardduty.types.data_source_free_trial.serialize_json(
            value["s3_logs"]
        )
    if "kubernetes" in value:
        import capo_guardduty.types.kubernetes_data_source_free_trial

        out["kubernetes"] = (
            capo_guardduty.types.kubernetes_data_source_free_trial.serialize_json(
                value["kubernetes"]
            )
        )
    if "malware_protection" in value:
        import capo_guardduty.types.malware_protection_data_source_free_trial

        out["malwareProtection"] = (
            capo_guardduty.types.malware_protection_data_source_free_trial.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourcesFreeTrial:
    out: DataSourcesFreeTrial = {}  # type: ignore[typeddict-item]
    if "cloudTrail" in data:
        import capo_guardduty.types.data_source_free_trial

        out["cloud_trail"] = (
            capo_guardduty.types.data_source_free_trial.deserialize_json(
                data["cloudTrail"]
            )
        )
    if "dnsLogs" in data:
        import capo_guardduty.types.data_source_free_trial

        out["dns_logs"] = capo_guardduty.types.data_source_free_trial.deserialize_json(
            data["dnsLogs"]
        )
    if "flowLogs" in data:
        import capo_guardduty.types.data_source_free_trial

        out["flow_logs"] = capo_guardduty.types.data_source_free_trial.deserialize_json(
            data["flowLogs"]
        )
    if "s3Logs" in data:
        import capo_guardduty.types.data_source_free_trial

        out["s3_logs"] = capo_guardduty.types.data_source_free_trial.deserialize_json(
            data["s3Logs"]
        )
    if "kubernetes" in data:
        import capo_guardduty.types.kubernetes_data_source_free_trial

        out["kubernetes"] = (
            capo_guardduty.types.kubernetes_data_source_free_trial.deserialize_json(
                data["kubernetes"]
            )
        )
    if "malwareProtection" in data:
        import capo_guardduty.types.malware_protection_data_source_free_trial

        out["malware_protection"] = (
            capo_guardduty.types.malware_protection_data_source_free_trial.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
