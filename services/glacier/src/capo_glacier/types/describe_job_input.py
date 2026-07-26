"""Generated from Smithy shape ``com.amazonaws.glacier#DescribeJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string


class DescribeJobInput(TypedDict, closed=True):
    account_id: "capo_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    vault_name: "capo_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    job_id: "capo_glacier.types.string.string"
    """<p>The ID of the job to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobInput:
    out: DescribeJobInput = {}  # type: ignore[typeddict-item]
    return out
