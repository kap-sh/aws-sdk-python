"""Generated from Smithy shape ``com.amazonaws.autoscaling#LocalStorageTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.local_storage_type

LocalStorageTypes: TypeAlias = list[
    "aws_sdk_auto_scaling.types.local_storage_type.LocalStorageType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LocalStorageTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.local_storage_type

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.local_storage_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LocalStorageTypes:
    import aws_sdk_auto_scaling.types.local_storage_type

    out: LocalStorageTypes = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.local_storage_type.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: LocalStorageTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.local_storage_type

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.local_storage_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LocalStorageTypes:
    import aws_sdk_auto_scaling.types.local_storage_type

    out: LocalStorageTypes = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.local_storage_type.deserialize_query(child)
        )
    return out
