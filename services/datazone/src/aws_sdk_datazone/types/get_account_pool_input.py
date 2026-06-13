"""Generated from Smithy shape ``com.amazonaws.datazone#GetAccountPoolInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_id
    import aws_sdk_datazone.types.domain_id


class GetAccountPoolInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which the account pool lives whose details are to be displayed.</p>"""
    identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId"
    """<p>The ID of the account pool whose details are to be displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountPoolInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountPoolInput:
    out: GetAccountPoolInput = {}  # type: ignore[typeddict-item]
    return out
