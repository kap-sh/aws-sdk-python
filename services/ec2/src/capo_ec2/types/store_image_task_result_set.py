"""Generated from Smithy shape ``com.amazonaws.ec2#StoreImageTaskResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.store_image_task_result

StoreImageTaskResultSet: TypeAlias = list[
    "capo_ec2.types.store_image_task_result.StoreImageTaskResult"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StoreImageTaskResultSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.store_image_task_result

        capo_ec2.types.store_image_task_result.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> StoreImageTaskResultSet:
    import capo_ec2.types.store_image_task_result

    out: StoreImageTaskResultSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.store_image_task_result.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> StoreImageTaskResultSet:
    import capo_ec2.types.store_image_task_result

    out: StoreImageTaskResultSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.store_image_task_result.deserialize_ec2_query(child))
    return out
