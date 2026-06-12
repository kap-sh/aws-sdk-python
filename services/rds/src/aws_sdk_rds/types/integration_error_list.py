"""Generated from Smithy shape ``com.amazonaws.rds#IntegrationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integration_error

IntegrationErrorList: TypeAlias = list[
    "aws_sdk_rds.types.integration_error.IntegrationError"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationErrorList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.integration_error

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.integration_error.serialize_query(
            item, pairs, f"{prefix}.IntegrationError.{n}"
        )


def deserialize_query(el: Element) -> IntegrationErrorList:
    import aws_sdk_rds.types.integration_error

    out: IntegrationErrorList = []
    for child in el.findall("IntegrationError"):
        out.append(aws_sdk_rds.types.integration_error.deserialize_query(child))
    return out


def serialize_query_flat(
    value: IntegrationErrorList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.integration_error

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.integration_error.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> IntegrationErrorList:
    import aws_sdk_rds.types.integration_error

    out: IntegrationErrorList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.integration_error.deserialize_query(child))
    return out
