"""Generated from Smithy shape ``com.amazonaws.ec2#DataResponses``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.data_response

DataResponses: TypeAlias = list["capo_ec2.types.data_response.DataResponse"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DataResponses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.data_response

        capo_ec2.types.data_response.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> DataResponses:
    import capo_ec2.types.data_response

    out: DataResponses = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.data_response.deserialize_ec2_query(child))
    return out
