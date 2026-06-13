"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQPersonalizationConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.personalization_mode
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateQPersonalizationConfigurationResponse(TypedDict):
    personalization_mode: NotRequired[
        "aws_sdk_quicksight.types.personalization_mode.PersonalizationMode"
    ]
    """<p>The personalization mode that is used for the personalization configuration.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQPersonalizationConfigurationResponse) -> dict:
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


def deserialize_json(data: dict) -> UpdateQPersonalizationConfigurationResponse:
    out: UpdateQPersonalizationConfigurationResponse = {}  # type: ignore[typeddict-item]
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
