"""Generated from Smithy shape ``com.amazonaws.grafana#IdpMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_grafana.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.idp_metadata_url


class _IdpMetadata_url(TypedDict, closed=True):
    url: "aws_sdk_grafana.types.idp_metadata_url.IdpMetadataUrl"


class _IdpMetadata_xml(TypedDict, closed=True):
    xml: "str"


IdpMetadata: TypeAlias = _IdpMetadata_url | _IdpMetadata_xml


# --- restJson1 ser/de ---
def serialize_json(value: IdpMetadata) -> dict:
    if "url" in value:
        return {"url": value["url"]}
    elif "xml" in value:
        return {"xml": value["xml"]}
    else:
        raise SerializationError("IdpMetadata: no variant present")


def deserialize_json(data: dict) -> IdpMetadata:
    if "url" in data:
        return {"url": data["url"]}
    elif "xml" in data:
        return {"xml": data["xml"]}
    else:
        raise DeserializationError("IdpMetadata: no recognized variant key")
