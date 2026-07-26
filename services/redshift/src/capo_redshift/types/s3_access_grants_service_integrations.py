"""Generated from Smithy shape ``com.amazonaws.redshift#S3AccessGrantsServiceIntegrations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.s3_access_grants_scope_union

S3AccessGrantsServiceIntegrations: TypeAlias = list[
    "capo_redshift.types.s3_access_grants_scope_union.S3AccessGrantsScopeUnion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: S3AccessGrantsServiceIntegrations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.s3_access_grants_scope_union

    for n, item in enumerate(value, 1):
        capo_redshift.types.s3_access_grants_scope_union.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> S3AccessGrantsServiceIntegrations:
    import capo_redshift.types.s3_access_grants_scope_union

    out: S3AccessGrantsServiceIntegrations = []
    for child in el.findall("member"):
        out.append(
            capo_redshift.types.s3_access_grants_scope_union.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: S3AccessGrantsServiceIntegrations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.s3_access_grants_scope_union

    for n, item in enumerate(value, 1):
        capo_redshift.types.s3_access_grants_scope_union.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> S3AccessGrantsServiceIntegrations:
    import capo_redshift.types.s3_access_grants_scope_union

    out: S3AccessGrantsServiceIntegrations = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.s3_access_grants_scope_union.deserialize_query(child)
        )
    return out
