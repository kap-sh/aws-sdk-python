"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_status_details

InstanceStatusDetailsList: TypeAlias = list[
    "capo_ec2.types.instance_status_details.InstanceStatusDetails"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatusDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_status_details

        capo_ec2.types.instance_status_details.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceStatusDetailsList:
    import capo_ec2.types.instance_status_details

    out: InstanceStatusDetailsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_status_details.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceStatusDetailsList:
    import capo_ec2.types.instance_status_details

    out: InstanceStatusDetailsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_status_details.deserialize_ec2_query(child))
    return out
