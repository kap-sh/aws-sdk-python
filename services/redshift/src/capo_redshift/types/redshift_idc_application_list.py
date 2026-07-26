"""Generated from Smithy shape ``com.amazonaws.redshift#RedshiftIdcApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.redshift_idc_application

RedshiftIdcApplicationList: TypeAlias = list[
    "capo_redshift.types.redshift_idc_application.RedshiftIdcApplication"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RedshiftIdcApplicationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.redshift_idc_application

    for n, item in enumerate(value, 1):
        capo_redshift.types.redshift_idc_application.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RedshiftIdcApplicationList:
    import capo_redshift.types.redshift_idc_application

    out: RedshiftIdcApplicationList = []
    for child in el.findall("member"):
        out.append(
            capo_redshift.types.redshift_idc_application.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RedshiftIdcApplicationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.redshift_idc_application

    for n, item in enumerate(value, 1):
        capo_redshift.types.redshift_idc_application.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RedshiftIdcApplicationList:
    import capo_redshift.types.redshift_idc_application

    out: RedshiftIdcApplicationList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.redshift_idc_application.deserialize_query(child)
        )
    return out
