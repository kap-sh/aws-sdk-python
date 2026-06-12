"""Generated from Smithy shape ``com.amazonaws.rds#ValidStorageOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.valid_storage_options

ValidStorageOptionsList: TypeAlias = list[
    "aws_sdk_rds.types.valid_storage_options.ValidStorageOptions"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidStorageOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.valid_storage_options

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.valid_storage_options.serialize_query(
            item, pairs, f"{prefix}.ValidStorageOptions.{n}"
        )


def deserialize_query(el: Element) -> ValidStorageOptionsList:
    import aws_sdk_rds.types.valid_storage_options

    out: ValidStorageOptionsList = []
    for child in el.findall("ValidStorageOptions"):
        out.append(aws_sdk_rds.types.valid_storage_options.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ValidStorageOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.valid_storage_options

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.valid_storage_options.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ValidStorageOptionsList:
    import aws_sdk_rds.types.valid_storage_options

    out: ValidStorageOptionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.valid_storage_options.deserialize_query(child))
    return out
