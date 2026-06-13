"""Generated from Smithy shape ``com.amazonaws.freetier#GetAccountActivityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.activity_id
    import aws_sdk_freetier.types.language_code


class GetAccountActivityRequest(TypedDict):
    activity_id: "aws_sdk_freetier.types.activity_id.ActivityId"
    """<p> A unique identifier that identifies the activity. </p>"""
    language_code: NotRequired["aws_sdk_freetier.types.language_code.LanguageCode"]
    """<p> The language code used to return translated title and description fields. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountActivityRequest) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    if "language_code" in value:
        import aws_sdk_freetier.types.language_code

        out["languageCode"] = (
            aws_sdk_freetier.types.language_code.serialize_aws_json_1_0(
                value["language_code"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountActivityRequest:
    out: GetAccountActivityRequest = {}  # type: ignore[typeddict-item]
    if "activityId" in data:
        out["activity_id"] = data["activityId"]
    else:
        raise DeserializationError("GetAccountActivityRequest.activity_id required")
    if "languageCode" in data:
        import aws_sdk_freetier.types.language_code

        out["language_code"] = (
            aws_sdk_freetier.types.language_code.deserialize_aws_json_1_0(
                data["languageCode"]
            )
        )
    return out
