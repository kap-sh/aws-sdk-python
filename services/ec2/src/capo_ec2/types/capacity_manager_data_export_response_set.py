"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportResponseSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_data_export_response

CapacityManagerDataExportResponseSet: TypeAlias = list[
    "capo_ec2.types.capacity_manager_data_export_response.CapacityManagerDataExportResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerDataExportResponseSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_manager_data_export_response

        capo_ec2.types.capacity_manager_data_export_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerDataExportResponseSet:
    import capo_ec2.types.capacity_manager_data_export_response

    out: CapacityManagerDataExportResponseSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_manager_data_export_response.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityManagerDataExportResponseSet:
    import capo_ec2.types.capacity_manager_data_export_response

    out: CapacityManagerDataExportResponseSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_manager_data_export_response.deserialize_ec2_query(
                child
            )
        )
    return out
