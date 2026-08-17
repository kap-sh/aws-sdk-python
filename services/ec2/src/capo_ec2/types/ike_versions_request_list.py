"""Generated from Smithy shape ``com.amazonaws.ec2#IKEVersionsRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ike_versions_request_list_value

IKEVersionsRequestList: TypeAlias = list[
    "capo_ec2.types.ike_versions_request_list_value.IKEVersionsRequestListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IKEVersionsRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ike_versions_request_list_value

        capo_ec2.types.ike_versions_request_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IKEVersionsRequestList:
    import capo_ec2.types.ike_versions_request_list_value

    out: IKEVersionsRequestList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ike_versions_request_list_value.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IKEVersionsRequestList:
    import capo_ec2.types.ike_versions_request_list_value

    out: IKEVersionsRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ike_versions_request_list_value.deserialize_ec2_query(child)
        )
    return out
