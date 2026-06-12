"""Generated from Smithy shape ``com.amazonaws.redshift#ParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.parameter

ParametersList: TypeAlias = list["aws_sdk_redshift.types.parameter.Parameter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ParametersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.parameter

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.parameter.serialize_query(
            item, pairs, f"{prefix}.Parameter.{n}"
        )


def deserialize_query(el: Element) -> ParametersList:
    import aws_sdk_redshift.types.parameter

    out: ParametersList = []
    for child in el.findall("Parameter"):
        out.append(aws_sdk_redshift.types.parameter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ParametersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.parameter

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.parameter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ParametersList:
    import aws_sdk_redshift.types.parameter

    out: ParametersList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.parameter.deserialize_query(child))
    return out
