"""Generated from Smithy shape ``com.amazonaws.redshift#RedshiftIdcApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.redshift_idc_application

RedshiftIdcApplicationList: TypeAlias = list[
    "aws_sdk_redshift.types.redshift_idc_application.RedshiftIdcApplication"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RedshiftIdcApplicationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.redshift_idc_application

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.redshift_idc_application.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RedshiftIdcApplicationList:
    import aws_sdk_redshift.types.redshift_idc_application

    out: RedshiftIdcApplicationList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_redshift.types.redshift_idc_application.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RedshiftIdcApplicationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.redshift_idc_application

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.redshift_idc_application.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RedshiftIdcApplicationList:
    import aws_sdk_redshift.types.redshift_idc_application

    out: RedshiftIdcApplicationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.redshift_idc_application.deserialize_query(child)
        )
    return out
