"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ListImageSetVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_set_properties_list
    import capo_medical_imaging.types.next_token


class ListImageSetVersionsResponse(TypedDict, closed=True):
    image_set_properties_list: (
        "capo_medical_imaging.types.image_set_properties_list.ImageSetPropertiesList"
    )
    """<p>Lists all properties associated with an image set.</p>"""
    next_token: NotRequired["capo_medical_imaging.types.next_token.NextToken"]
    """<p>The pagination token used to retrieve the list of image set versions on the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageSetVersionsResponse) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.image_set_properties_list

    out["imageSetPropertiesList"] = (
        capo_medical_imaging.types.image_set_properties_list.serialize_json(
            value["image_set_properties_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageSetVersionsResponse:
    out: ListImageSetVersionsResponse = {}  # type: ignore[typeddict-item]
    if "imageSetPropertiesList" in data:
        import capo_medical_imaging.types.image_set_properties_list

        out["image_set_properties_list"] = (
            capo_medical_imaging.types.image_set_properties_list.deserialize_json(
                data["imageSetPropertiesList"]
            )
        )
    else:
        raise DeserializationError(
            "ListImageSetVersionsResponse.image_set_properties_list required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
