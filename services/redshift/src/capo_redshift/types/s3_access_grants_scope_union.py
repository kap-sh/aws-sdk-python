"""Generated from Smithy shape ``com.amazonaws.redshift#S3AccessGrantsScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_redshift.types.read_write_access


class _S3AccessGrantsScopeUnion_ReadWriteAccess(TypedDict, closed=True):
    ReadWriteAccess: "capo_redshift.types.read_write_access.ReadWriteAccess"


S3AccessGrantsScopeUnion: TypeAlias = _S3AccessGrantsScopeUnion_ReadWriteAccess


# --- awsQuery ser/de ---
def serialize_query(
    value: S3AccessGrantsScopeUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ReadWriteAccess" in value:
        import capo_redshift.types.read_write_access

        capo_redshift.types.read_write_access.serialize_query(
            value["ReadWriteAccess"], pairs, f"{prefix}.ReadWriteAccess"
        )
    else:
        raise SerializationError("S3AccessGrantsScopeUnion: no variant present")


def deserialize_query(el: Element) -> S3AccessGrantsScopeUnion:
    for child in el:
        if child.tag == "ReadWriteAccess":
            import capo_redshift.types.read_write_access

            return {
                "ReadWriteAccess": capo_redshift.types.read_write_access.deserialize_query(
                    child
                )
            }
    raise DeserializationError(
        "S3AccessGrantsScopeUnion: no recognized variant element"
    )
