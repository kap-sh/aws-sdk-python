"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyHostsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.response_host_id_list
    import capo_ec2.types.unsuccessful_item_list


class ModifyHostsResult(TypedDict, closed=True):
    successful: NotRequired["capo_ec2.types.response_host_id_list.ResponseHostIdList"]
    """<p>The IDs of the Dedicated Hosts that were successfully modified.</p>"""
    unsuccessful: NotRequired[
        "capo_ec2.types.unsuccessful_item_list.UnsuccessfulItemList"
    ]
    """<p>The IDs of the Dedicated Hosts that could not be modified. Check whether the setting you requested can be used.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyHostsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful" in value:
        import capo_ec2.types.response_host_id_list

        capo_ec2.types.response_host_id_list.serialize_ec2_query(
            value["successful"], pairs, f"{prefix}.Successful"
        )
    if "unsuccessful" in value:
        import capo_ec2.types.unsuccessful_item_list

        capo_ec2.types.unsuccessful_item_list.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{prefix}.Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> ModifyHostsResult:
    out: ModifyHostsResult = {}  # type: ignore[typeddict-item]
    if el.find("Successful") is not None:
        import capo_ec2.types.response_host_id_list

        out["successful"] = capo_ec2.types.response_host_id_list.deserialize_ec2_query(
            el, "Successful"
        )
    if el.find("Unsuccessful") is not None:
        import capo_ec2.types.unsuccessful_item_list

        out["unsuccessful"] = (
            capo_ec2.types.unsuccessful_item_list.deserialize_ec2_query(
                el, "Unsuccessful"
            )
        )
    return out
