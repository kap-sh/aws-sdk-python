"""Generated from Smithy shape ``com.amazonaws.ivs#ImportPlaybackKeyPairRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_key_pair_name
    import aws_sdk_ivs.types.playback_public_key_material
    import aws_sdk_ivs.types.tags


class ImportPlaybackKeyPairRequest(TypedDict):
    public_key_material: (
        "aws_sdk_ivs.types.playback_public_key_material.PlaybackPublicKeyMaterial"
    )
    """<p>The public portion of a customer-generated key pair.</p>"""
    name: NotRequired["aws_sdk_ivs.types.playback_key_pair_name.PlaybackKeyPairName"]
    """<p>Playback-key-pair name. The value does not need to be unique.</p>"""
    tags: NotRequired["aws_sdk_ivs.types.tags.Tags"]
    """<p>Any tags provided with the request are added to the playback key pair tags. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPlaybackKeyPairRequest) -> dict:
    out: dict = {}
    out["publicKeyMaterial"] = value["public_key_material"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ImportPlaybackKeyPairRequest:
    out: ImportPlaybackKeyPairRequest = {}  # type: ignore[typeddict-item]
    if "publicKeyMaterial" in data:
        out["public_key_material"] = data["publicKeyMaterial"]
    else:
        raise DeserializationError(
            "ImportPlaybackKeyPairRequest.public_key_material required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.deserialize_json(data["tags"])
    return out
