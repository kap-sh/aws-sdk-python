"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalStrategyResponse``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mpa.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.mof_n_approval_strategy


class _ApprovalStrategyResponse_MofN(TypedDict):
    MofN: "aws_sdk_mpa.types.mof_n_approval_strategy.MofNApprovalStrategy"


ApprovalStrategyResponse: TypeAlias = _ApprovalStrategyResponse_MofN


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStrategyResponse) -> dict:
    if "MofN" in value:
        import aws_sdk_mpa.types.mof_n_approval_strategy

        return {
            "MofN": aws_sdk_mpa.types.mof_n_approval_strategy.serialize_json(
                value["MofN"]
            )
        }
    else:
        raise SerializationError("ApprovalStrategyResponse: no variant present")


def deserialize_json(data: dict) -> ApprovalStrategyResponse:
    if "MofN" in data:
        import aws_sdk_mpa.types.mof_n_approval_strategy

        return {
            "MofN": aws_sdk_mpa.types.mof_n_approval_strategy.deserialize_json(
                data["MofN"]
            )
        }
    else:
        raise DeserializationError(
            "ApprovalStrategyResponse: no recognized variant key"
        )
