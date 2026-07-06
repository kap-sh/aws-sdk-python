"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQPersonalizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.personalization_mode


class UpdateQPersonalizationConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account account that contains the personalization configuration that the user wants to update.</p>"""
    personalization_mode: (
        "aws_sdk_quicksight.types.personalization_mode.PersonalizationMode"
    )
    """<p>An option to allow Amazon Quick Sight to customize data stories with user specific metadata, specifically location and job information, in your IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQPersonalizationConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.personalization_mode

    out["PersonalizationMode"] = (
        aws_sdk_quicksight.types.personalization_mode.serialize_json(
            value["personalization_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQPersonalizationConfigurationRequest:
    out: UpdateQPersonalizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "PersonalizationMode" in data:
        import aws_sdk_quicksight.types.personalization_mode

        out["personalization_mode"] = (
            aws_sdk_quicksight.types.personalization_mode.deserialize_json(
                data["PersonalizationMode"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQPersonalizationConfigurationRequest.personalization_mode required"
        )
    return out
