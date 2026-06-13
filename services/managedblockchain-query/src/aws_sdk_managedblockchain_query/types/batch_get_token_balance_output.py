"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_errors
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_list


class BatchGetTokenBalanceOutput(TypedDict):
    token_balances: "aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_list.BatchGetTokenBalanceOutputList"
    """<p>An array of <code>BatchGetTokenBalanceOutputItem</code> objects returned by the response.</p>"""
    errors: "aws_sdk_managedblockchain_query.types.batch_get_token_balance_errors.BatchGetTokenBalanceErrors"
    """<p>An array of <code>BatchGetTokenBalanceErrorItem</code> objects returned from the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceOutput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_list

    out["tokenBalances"] = (
        aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_list.serialize_json(
            value["token_balances"]
        )
    )
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_errors

    out["errors"] = (
        aws_sdk_managedblockchain_query.types.batch_get_token_balance_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceOutput:
    out: BatchGetTokenBalanceOutput = {}  # type: ignore[typeddict-item]
    if "tokenBalances" in data:
        import aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_list

        out["token_balances"] = (
            aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_list.deserialize_json(
                data["tokenBalances"]
            )
        )
    else:
        raise DeserializationError("BatchGetTokenBalanceOutput.token_balances required")
    if "errors" in data:
        import aws_sdk_managedblockchain_query.types.batch_get_token_balance_errors

        out["errors"] = (
            aws_sdk_managedblockchain_query.types.batch_get_token_balance_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetTokenBalanceOutput.errors required")
    return out
