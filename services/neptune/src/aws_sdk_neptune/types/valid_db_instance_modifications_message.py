"""Generated from Smithy shape ``com.amazonaws.neptune#ValidDBInstanceModificationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.valid_storage_options_list


class ValidDBInstanceModificationsMessage(TypedDict, closed=True):
    storage: NotRequired[
        "aws_sdk_neptune.types.valid_storage_options_list.ValidStorageOptionsList"
    ]
    """<p>Valid storage options for your DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidDBInstanceModificationsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "storage" in value:
        import aws_sdk_neptune.types.valid_storage_options_list

        aws_sdk_neptune.types.valid_storage_options_list.serialize_query(
            value["storage"], pairs, f"{prefix}.Storage"
        )


def deserialize_query(el: Element) -> ValidDBInstanceModificationsMessage:
    out: ValidDBInstanceModificationsMessage = {}  # type: ignore[typeddict-item]
    child_storage = el.find("Storage")
    if child_storage is not None:
        import aws_sdk_neptune.types.valid_storage_options_list

        out["storage"] = (
            aws_sdk_neptune.types.valid_storage_options_list.deserialize_query(
                child_storage
            )
        )
    return out
