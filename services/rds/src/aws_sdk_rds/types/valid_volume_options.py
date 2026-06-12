"""Generated from Smithy shape ``com.amazonaws.rds#ValidVolumeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.valid_storage_options_list


class ValidVolumeOptions(TypedDict):
    volume_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the additional storage volume.</p>"""
    storage: NotRequired[
        "aws_sdk_rds.types.valid_storage_options_list.ValidStorageOptionsList"
    ]
    """<p>The valid storage options for the additional storage volume.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidVolumeOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volume_name" in value:
        pairs.append((f"{prefix}.VolumeName", str(value["volume_name"])))
    if "storage" in value:
        import aws_sdk_rds.types.valid_storage_options_list

        aws_sdk_rds.types.valid_storage_options_list.serialize_query(
            value["storage"], pairs, f"{prefix}.Storage"
        )


def deserialize_query(el: Element) -> ValidVolumeOptions:
    out: ValidVolumeOptions = {}  # type: ignore[typeddict-item]
    child_volume_name = el.find("VolumeName")
    if child_volume_name is not None:
        out["volume_name"] = str(child_volume_name.text or "")
    child_storage = el.find("Storage")
    if child_storage is not None:
        import aws_sdk_rds.types.valid_storage_options_list

        out["storage"] = aws_sdk_rds.types.valid_storage_options_list.deserialize_query(
            child_storage
        )
    return out
