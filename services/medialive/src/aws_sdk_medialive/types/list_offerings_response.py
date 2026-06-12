"""Generated from Smithy shape ``com.amazonaws.medialive#ListOfferingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_offering
    import aws_sdk_medialive.types.__string


class ListOfferingsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token to retrieve the next page of results"""
    offerings: NotRequired[
        "aws_sdk_medialive.types.__list_of_offering.__listOfOffering"
    ]
    """List of offerings"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOfferingsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "offerings" in value:
        import aws_sdk_medialive.types.__list_of_offering

        out["offerings"] = aws_sdk_medialive.types.__list_of_offering.serialize_json(
            value["offerings"]
        )
    return out


def deserialize_json(data: dict) -> ListOfferingsResponse:
    out: ListOfferingsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "offerings" in data:
        import aws_sdk_medialive.types.__list_of_offering

        out["offerings"] = aws_sdk_medialive.types.__list_of_offering.deserialize_json(
            data["offerings"]
        )
    return out
