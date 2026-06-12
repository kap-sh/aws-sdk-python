"""Generated from Smithy shape ``com.amazonaws.elasticache#ParameterNameValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.parameter_name_value

ParameterNameValueList: TypeAlias = list[
    "aws_sdk_elasticache.types.parameter_name_value.ParameterNameValue"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterNameValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.parameter_name_value

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.parameter_name_value.serialize_query(
            item, pairs, f"{prefix}.ParameterNameValue.{n}"
        )


def deserialize_query(el: Element) -> ParameterNameValueList:
    import aws_sdk_elasticache.types.parameter_name_value

    out: ParameterNameValueList = []
    for child in el.findall("ParameterNameValue"):
        out.append(
            aws_sdk_elasticache.types.parameter_name_value.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ParameterNameValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.parameter_name_value

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.parameter_name_value.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ParameterNameValueList:
    import aws_sdk_elasticache.types.parameter_name_value

    out: ParameterNameValueList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.parameter_name_value.deserialize_query(child)
        )
    return out
