"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.get_token_balance_input_list


class BatchGetTokenBalanceInput(TypedDict, closed=True):
    get_token_balance_inputs: NotRequired[
        "aws_sdk_managedblockchain_query.types.get_token_balance_input_list.GetTokenBalanceInputList"
    ]
    """<p>An array of <code>BatchGetTokenBalanceInputItem</code> objects whose balance is being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceInput) -> dict:
    out: dict = {}
    if "get_token_balance_inputs" in value:
        import aws_sdk_managedblockchain_query.types.get_token_balance_input_list

        out["getTokenBalanceInputs"] = (
            aws_sdk_managedblockchain_query.types.get_token_balance_input_list.serialize_json(
                value["get_token_balance_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceInput:
    out: BatchGetTokenBalanceInput = {}  # type: ignore[typeddict-item]
    if "getTokenBalanceInputs" in data:
        import aws_sdk_managedblockchain_query.types.get_token_balance_input_list

        out["get_token_balance_inputs"] = (
            aws_sdk_managedblockchain_query.types.get_token_balance_input_list.deserialize_json(
                data["getTokenBalanceInputs"]
            )
        )
    return out
