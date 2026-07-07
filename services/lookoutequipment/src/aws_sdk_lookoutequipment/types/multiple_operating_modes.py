"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MultipleOperatingModes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.statistical_issue_status


class MultipleOperatingModes(TypedDict, closed=True):
    status: (
        "aws_sdk_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to having multiple operating modes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultipleOperatingModes) -> dict:
    out: dict = {}
    import aws_sdk_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        aws_sdk_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultipleOperatingModes:
    out: MultipleOperatingModes = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.statistical_issue_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.statistical_issue_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("MultipleOperatingModes.status required")
    return out
