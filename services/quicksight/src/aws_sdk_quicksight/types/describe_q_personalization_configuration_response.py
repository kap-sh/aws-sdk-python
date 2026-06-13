"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeQPersonalizationConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.personalization_mode
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeQPersonalizationConfigurationResponse(TypedDict):
    personalization_mode: NotRequired[
        "aws_sdk_quicksight.types.personalization_mode.PersonalizationMode"
    ]
    """<p>A value that indicates whether personalization is enabled or not.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQPersonalizationConfigurationResponse) -> dict:
    out: dict = {}
    if "personalization_mode" in value:
        import aws_sdk_quicksight.types.personalization_mode

        out["PersonalizationMode"] = (
            aws_sdk_quicksight.types.personalization_mode.serialize_json(
                value["personalization_mode"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeQPersonalizationConfigurationResponse:
    out: DescribeQPersonalizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "PersonalizationMode" in data:
        import aws_sdk_quicksight.types.personalization_mode

        out["personalization_mode"] = (
            aws_sdk_quicksight.types.personalization_mode.deserialize_json(
                data["PersonalizationMode"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
