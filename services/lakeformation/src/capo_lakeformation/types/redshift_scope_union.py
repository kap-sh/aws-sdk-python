"""Generated from Smithy shape ``com.amazonaws.lakeformation#RedshiftScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.redshift_connect


class _RedshiftScopeUnion_RedshiftConnect(TypedDict, closed=True):
    RedshiftConnect: "capo_lakeformation.types.redshift_connect.RedshiftConnect"


RedshiftScopeUnion: TypeAlias = _RedshiftScopeUnion_RedshiftConnect


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftScopeUnion) -> dict:
    if "RedshiftConnect" in value:
        import capo_lakeformation.types.redshift_connect

        return {
            "RedshiftConnect": capo_lakeformation.types.redshift_connect.serialize_json(
                value["RedshiftConnect"]
            )
        }
    else:
        raise SerializationError("RedshiftScopeUnion: no variant present")


def deserialize_json(data: dict) -> RedshiftScopeUnion:
    if "RedshiftConnect" in data:
        import capo_lakeformation.types.redshift_connect

        return {
            "RedshiftConnect": capo_lakeformation.types.redshift_connect.deserialize_json(
                data["RedshiftConnect"]
            )
        }
    else:
        raise DeserializationError("RedshiftScopeUnion: no recognized variant key")
