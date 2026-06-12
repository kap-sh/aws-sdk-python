"""Generated from Smithy shape ``com.amazonaws.redshift#RedshiftScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.connect


class _RedshiftScopeUnion_Connect(TypedDict):
    Connect: "aws_sdk_redshift.types.connect.Connect"


RedshiftScopeUnion: TypeAlias = _RedshiftScopeUnion_Connect


# --- awsQuery ser/de ---
def serialize_query(
    value: RedshiftScopeUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "Connect" in value:
        import aws_sdk_redshift.types.connect

        aws_sdk_redshift.types.connect.serialize_query(
            value["Connect"], pairs, f"{prefix}.Connect"
        )
    else:
        raise SerializationError("RedshiftScopeUnion: no variant present")


def deserialize_query(el: Element) -> RedshiftScopeUnion:
    for child in el:
        if child.tag == "Connect":
            import aws_sdk_redshift.types.connect

            return {"Connect": aws_sdk_redshift.types.connect.deserialize_query(child)}
    raise DeserializationError("RedshiftScopeUnion: no recognized variant element")
