"""Generated from Smithy shape ``com.amazonaws.rds#ValidVolumeOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.valid_volume_options

ValidVolumeOptionsList: TypeAlias = list[
    "aws_sdk_rds.types.valid_volume_options.ValidVolumeOptions"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidVolumeOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.valid_volume_options

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.valid_volume_options.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ValidVolumeOptionsList:
    import aws_sdk_rds.types.valid_volume_options

    out: ValidVolumeOptionsList = []
    for child in el.findall("member"):
        out.append(aws_sdk_rds.types.valid_volume_options.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ValidVolumeOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.valid_volume_options

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.valid_volume_options.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ValidVolumeOptionsList:
    import aws_sdk_rds.types.valid_volume_options

    out: ValidVolumeOptionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.valid_volume_options.deserialize_query(child))
    return out
