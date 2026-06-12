"""Generated from Smithy shape ``com.amazonaws.macie2#ListResourceProfileDetectionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_detection
    import aws_sdk_macie2.types.__string


class ListResourceProfileDetectionsResponse(TypedDict):
    detections: NotRequired[
        "aws_sdk_macie2.types.__list_of_detection.__listOfDetection"
    ]
    """<p>An array of objects, one for each type of sensitive data that Amazon Macie found in the bucket. Each object reports the number of occurrences of the specified type and provides information about the custom data identifier or managed data identifier that detected the data.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceProfileDetectionsResponse) -> dict:
    out: dict = {}
    if "detections" in value:
        import aws_sdk_macie2.types.__list_of_detection

        out["detections"] = aws_sdk_macie2.types.__list_of_detection.serialize_json(
            value["detections"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceProfileDetectionsResponse:
    out: ListResourceProfileDetectionsResponse = {}  # type: ignore[typeddict-item]
    if "detections" in data:
        import aws_sdk_macie2.types.__list_of_detection

        out["detections"] = aws_sdk_macie2.types.__list_of_detection.deserialize_json(
            data["detections"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
