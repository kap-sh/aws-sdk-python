"""Generated from Smithy shape ``com.amazonaws.redshift#LakeFormationServiceIntegrations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.lake_formation_scope_union

LakeFormationServiceIntegrations: TypeAlias = list[
    "capo_redshift.types.lake_formation_scope_union.LakeFormationScopeUnion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LakeFormationServiceIntegrations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.lake_formation_scope_union

    for n, item in enumerate(value, 1):
        capo_redshift.types.lake_formation_scope_union.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LakeFormationServiceIntegrations:
    import capo_redshift.types.lake_formation_scope_union

    out: LakeFormationServiceIntegrations = []
    for child in el.findall("member"):
        out.append(
            capo_redshift.types.lake_formation_scope_union.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: LakeFormationServiceIntegrations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.lake_formation_scope_union

    for n, item in enumerate(value, 1):
        capo_redshift.types.lake_formation_scope_union.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> LakeFormationServiceIntegrations:
    import capo_redshift.types.lake_formation_scope_union

    out: LakeFormationServiceIntegrations = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.lake_formation_scope_union.deserialize_query(child)
        )
    return out
