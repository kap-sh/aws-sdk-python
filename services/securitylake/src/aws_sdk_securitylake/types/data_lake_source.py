"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_source_status_list
    import aws_sdk_securitylake.types.ocsf_event_class_list


class DataLakeSource(TypedDict):
    account: NotRequired["str"]
    """<p>The ID of the Security Lake account for which logs are collected.</p>"""
    source_name: NotRequired["str"]
    """<p>The supported Amazon Web Services services from which logs and events are collected. Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>"""
    event_classes: NotRequired[
        "aws_sdk_securitylake.types.ocsf_event_class_list.OcsfEventClassList"
    ]
    r"""<p>The Open Cybersecurity Schema Framework (OCSF) event classes describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass.html\">Supported OCSF Event classes</a> in the Amazon Security Lake User Guide.</p>"""
    source_statuses: NotRequired[
        "aws_sdk_securitylake.types.data_lake_source_status_list.DataLakeSourceStatusList"
    ]
    """<p>The log status for the Security Lake account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSource) -> dict:
    out: dict = {}
    if "account" in value:
        out["account"] = value["account"]
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    if "event_classes" in value:
        import aws_sdk_securitylake.types.ocsf_event_class_list

        out["eventClasses"] = (
            aws_sdk_securitylake.types.ocsf_event_class_list.serialize_json(
                value["event_classes"]
            )
        )
    if "source_statuses" in value:
        import aws_sdk_securitylake.types.data_lake_source_status_list

        out["sourceStatuses"] = (
            aws_sdk_securitylake.types.data_lake_source_status_list.serialize_json(
                value["source_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeSource:
    out: DataLakeSource = {}  # type: ignore[typeddict-item]
    if "account" in data:
        out["account"] = data["account"]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    if "eventClasses" in data:
        import aws_sdk_securitylake.types.ocsf_event_class_list

        out["event_classes"] = (
            aws_sdk_securitylake.types.ocsf_event_class_list.deserialize_json(
                data["eventClasses"]
            )
        )
    if "sourceStatuses" in data:
        import aws_sdk_securitylake.types.data_lake_source_status_list

        out["source_statuses"] = (
            aws_sdk_securitylake.types.data_lake_source_status_list.deserialize_json(
                data["sourceStatuses"]
            )
        )
    return out
