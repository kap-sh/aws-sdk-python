"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFlowLogsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.unsuccessful_item_set
    import capo_ec2.types.value_string_list


class CreateFlowLogsResult(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    flow_log_ids: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the flow logs.</p>"""
    unsuccessful: NotRequired[
        "capo_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the flow logs that could not be created successfully.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFlowLogsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "flow_log_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["flow_log_ids"], pairs, f"{key_prefix}FlowLogIdSet"
        )
    if "unsuccessful" in value:
        import capo_ec2.types.unsuccessful_item_set

        capo_ec2.types.unsuccessful_item_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{key_prefix}Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> CreateFlowLogsResult:
    out: CreateFlowLogsResult = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    if el.find("flowLogIdSet") is not None:
        import capo_ec2.types.value_string_list

        out["flow_log_ids"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "flowLogIdSet"
        )
    if el.find("unsuccessful") is not None:
        import capo_ec2.types.unsuccessful_item_set

        out["unsuccessful"] = (
            capo_ec2.types.unsuccessful_item_set.deserialize_ec2_query(
                el, "unsuccessful"
            )
        )
    return out
