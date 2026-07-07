"""Generated from Smithy shape ``com.amazonaws.support#DescribeSeverityLevelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.severity_levels_list


class DescribeSeverityLevelsResponse(TypedDict, closed=True):
    severity_levels: NotRequired[
        "aws_sdk_support.types.severity_levels_list.SeverityLevelsList"
    ]
    """<p>The available severity levels for the support case. Available severity levels are defined by your service level agreement with Amazon Web Services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSeverityLevelsResponse) -> dict:
    out: dict = {}
    if "severity_levels" in value:
        import aws_sdk_support.types.severity_levels_list

        out["severityLevels"] = (
            aws_sdk_support.types.severity_levels_list.serialize_aws_json_1_1(
                value["severity_levels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSeverityLevelsResponse:
    out: DescribeSeverityLevelsResponse = {}  # type: ignore[typeddict-item]
    if "severityLevels" in data:
        import aws_sdk_support.types.severity_levels_list

        out["severity_levels"] = (
            aws_sdk_support.types.severity_levels_list.deserialize_aws_json_1_1(
                data["severityLevels"]
            )
        )
    return out
