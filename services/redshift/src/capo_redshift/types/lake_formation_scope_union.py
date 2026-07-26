"""Generated from Smithy shape ``com.amazonaws.redshift#LakeFormationScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_redshift.types.lake_formation_query


class _LakeFormationScopeUnion_LakeFormationQuery(TypedDict, closed=True):
    LakeFormationQuery: "capo_redshift.types.lake_formation_query.LakeFormationQuery"


LakeFormationScopeUnion: TypeAlias = _LakeFormationScopeUnion_LakeFormationQuery


# --- awsQuery ser/de ---
def serialize_query(
    value: LakeFormationScopeUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "LakeFormationQuery" in value:
        import capo_redshift.types.lake_formation_query

        capo_redshift.types.lake_formation_query.serialize_query(
            value["LakeFormationQuery"], pairs, f"{prefix}.LakeFormationQuery"
        )
    else:
        raise SerializationError("LakeFormationScopeUnion: no variant present")


def deserialize_query(el: Element) -> LakeFormationScopeUnion:
    for child in el:
        if child.tag == "LakeFormationQuery":
            import capo_redshift.types.lake_formation_query

            return {
                "LakeFormationQuery": capo_redshift.types.lake_formation_query.deserialize_query(
                    child
                )
            }
    raise DeserializationError("LakeFormationScopeUnion: no recognized variant element")
