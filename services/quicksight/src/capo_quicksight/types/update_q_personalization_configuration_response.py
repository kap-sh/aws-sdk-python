"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQPersonalizationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.personalization_mode
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateQPersonalizationConfigurationResponse(TypedDict, closed=True):
    personalization_mode: NotRequired[
        "capo_quicksight.types.personalization_mode.PersonalizationMode"
    ]
    """<p>The personalization mode that is used for the personalization configuration.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQPersonalizationConfigurationResponse) -> dict:
    out: dict = {}
    if "personalization_mode" in value:
        import capo_quicksight.types.personalization_mode

        out["PersonalizationMode"] = (
            capo_quicksight.types.personalization_mode.serialize_json(
                value["personalization_mode"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateQPersonalizationConfigurationResponse:
    out: UpdateQPersonalizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "PersonalizationMode" in data:
        import capo_quicksight.types.personalization_mode

        out["personalization_mode"] = (
            capo_quicksight.types.personalization_mode.deserialize_json(
                data["PersonalizationMode"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
