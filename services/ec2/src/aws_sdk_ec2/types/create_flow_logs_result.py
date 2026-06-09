"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFlowLogsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unsuccessful_item_set
    import aws_sdk_ec2.types.value_string_list


class CreateFlowLogsResult(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    flow_log_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the flow logs.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the flow logs that could not be created successfully.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFlowLogsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "flow_log_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["flow_log_ids"], pairs, f"{prefix}.FlowLogIdSet"
        )
    if "unsuccessful" in value:
        import aws_sdk_ec2.types.unsuccessful_item_set

        aws_sdk_ec2.types.unsuccessful_item_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{prefix}.Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> CreateFlowLogsResult:
    out: CreateFlowLogsResult = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    if el.find("FlowLogIdSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["flow_log_ids"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "FlowLogIdSet"
        )
    if el.find("Unsuccessful") is not None:
        import aws_sdk_ec2.types.unsuccessful_item_set

        out["unsuccessful"] = (
            aws_sdk_ec2.types.unsuccessful_item_set.deserialize_ec2_query(
                el, "Unsuccessful"
            )
        )
    return out
