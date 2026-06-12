"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopyImageSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.copy_destination_image_set_properties
    import aws_sdk_medical_imaging.types.copy_source_image_set_properties
    import aws_sdk_medical_imaging.types.datastore_id


class CopyImageSetResponse(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    source_image_set_properties: "aws_sdk_medical_imaging.types.copy_source_image_set_properties.CopySourceImageSetProperties"
    """<p>The properties of the source image set.</p>"""
    destination_image_set_properties: "aws_sdk_medical_imaging.types.copy_destination_image_set_properties.CopyDestinationImageSetProperties"
    """<p>The properties of the destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyImageSetResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    import aws_sdk_medical_imaging.types.copy_source_image_set_properties

    out["sourceImageSetProperties"] = (
        aws_sdk_medical_imaging.types.copy_source_image_set_properties.serialize_json(
            value["source_image_set_properties"]
        )
    )
    import aws_sdk_medical_imaging.types.copy_destination_image_set_properties

    out["destinationImageSetProperties"] = (
        aws_sdk_medical_imaging.types.copy_destination_image_set_properties.serialize_json(
            value["destination_image_set_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> CopyImageSetResponse:
    out: CopyImageSetResponse = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("CopyImageSetResponse.datastore_id required")
    if "sourceImageSetProperties" in data:
        import aws_sdk_medical_imaging.types.copy_source_image_set_properties

        out["source_image_set_properties"] = (
            aws_sdk_medical_imaging.types.copy_source_image_set_properties.deserialize_json(
                data["sourceImageSetProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CopyImageSetResponse.source_image_set_properties required"
        )
    if "destinationImageSetProperties" in data:
        import aws_sdk_medical_imaging.types.copy_destination_image_set_properties

        out["destination_image_set_properties"] = (
            aws_sdk_medical_imaging.types.copy_destination_image_set_properties.deserialize_json(
                data["destinationImageSetProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CopyImageSetResponse.destination_image_set_properties required"
        )
    return out
