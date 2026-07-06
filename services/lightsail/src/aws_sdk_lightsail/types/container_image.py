"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.string


class ContainerImage(TypedDict, closed=True):
    image: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name of the container image.</p>"""
    digest: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The digest of the container image.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the container image was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerImage) -> dict:
    out: dict = {}
    if "image" in value:
        out["image"] = value["image"]
    if "digest" in value:
        out["digest"] = value["digest"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerImage:
    out: ContainerImage = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    if "digest" in data:
        out["digest"] = data["digest"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out
