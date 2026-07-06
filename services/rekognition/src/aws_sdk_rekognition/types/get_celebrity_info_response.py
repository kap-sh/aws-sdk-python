"""Generated from Smithy shape ``com.amazonaws.rekognition#GetCelebrityInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.known_gender
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.urls


class GetCelebrityInfoResponse(TypedDict, closed=True):
    urls: NotRequired["aws_sdk_rekognition.types.urls.Urls"]
    """<p>An array of URLs pointing to additional celebrity information. </p>"""
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The name of the celebrity.</p>"""
    known_gender: NotRequired["aws_sdk_rekognition.types.known_gender.KnownGender"]
    """<p>Retrieves the known gender for the celebrity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCelebrityInfoResponse) -> dict:
    out: dict = {}
    if "urls" in value:
        import aws_sdk_rekognition.types.urls

        out["Urls"] = aws_sdk_rekognition.types.urls.serialize_aws_json_1_1(
            value["urls"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "known_gender" in value:
        import aws_sdk_rekognition.types.known_gender

        out["KnownGender"] = (
            aws_sdk_rekognition.types.known_gender.serialize_aws_json_1_1(
                value["known_gender"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCelebrityInfoResponse:
    out: GetCelebrityInfoResponse = {}  # type: ignore[typeddict-item]
    if "Urls" in data:
        import aws_sdk_rekognition.types.urls

        out["urls"] = aws_sdk_rekognition.types.urls.deserialize_aws_json_1_1(
            data["Urls"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "KnownGender" in data:
        import aws_sdk_rekognition.types.known_gender

        out["known_gender"] = (
            aws_sdk_rekognition.types.known_gender.deserialize_aws_json_1_1(
                data["KnownGender"]
            )
        )
    return out
