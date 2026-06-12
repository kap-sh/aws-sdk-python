"""Generated from Smithy shape ``com.amazonaws.redshift#LakeFormationScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.lake_formation_query


class _LakeFormationScopeUnion_LakeFormationQuery(TypedDict):
    LakeFormationQuery: "aws_sdk_redshift.types.lake_formation_query.LakeFormationQuery"


LakeFormationScopeUnion: TypeAlias = _LakeFormationScopeUnion_LakeFormationQuery


# --- awsQuery ser/de ---
def serialize_query(
    value: LakeFormationScopeUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "LakeFormationQuery" in value:
        import aws_sdk_redshift.types.lake_formation_query

        aws_sdk_redshift.types.lake_formation_query.serialize_query(
            value["LakeFormationQuery"], pairs, f"{prefix}.LakeFormationQuery"
        )
    else:
        raise SerializationError("LakeFormationScopeUnion: no variant present")


def deserialize_query(el: Element) -> LakeFormationScopeUnion:
    for child in el:
        if child.tag == "LakeFormationQuery":
            import aws_sdk_redshift.types.lake_formation_query

            return {
                "LakeFormationQuery": aws_sdk_redshift.types.lake_formation_query.deserialize_query(
                    child
                )
            }
    raise DeserializationError("LakeFormationScopeUnion: no recognized variant element")
