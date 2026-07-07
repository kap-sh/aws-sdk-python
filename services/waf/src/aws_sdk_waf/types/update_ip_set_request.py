"""Generated from Smithy shape ``com.amazonaws.waf#UpdateIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.ip_set_updates
    import aws_sdk_waf.types.resource_id


class UpdateIPSetRequest(TypedDict, closed=True):
    ip_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to update. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "aws_sdk_waf.types.ip_set_updates.IPSetUpdates"
    """<p>An array of <code>IPSetUpdate</code> objects that you want to insert into or delete from an <a>IPSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>IPSetUpdate</a>: Contains <code>Action</code> and <code>IPSetDescriptor</code> </p> </li> <li> <p> <a>IPSetDescriptor</a>: Contains <code>Type</code> and <code>Value</code> </p> </li> </ul> <p>You can insert a maximum of 1000 addresses in a single request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIPSetRequest) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    out["ChangeToken"] = value["change_token"]
    import aws_sdk_waf.types.ip_set_updates

    out["Updates"] = aws_sdk_waf.types.ip_set_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIPSetRequest:
    out: UpdateIPSetRequest = {}  # type: ignore[typeddict-item]
    if "IPSetId" in data:
        out["ip_set_id"] = data["IPSetId"]
    else:
        raise DeserializationError("UpdateIPSetRequest.ip_set_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateIPSetRequest.change_token required")
    if "Updates" in data:
        import aws_sdk_waf.types.ip_set_updates

        out["updates"] = aws_sdk_waf.types.ip_set_updates.deserialize_aws_json_1_1(
            data["Updates"]
        )
    else:
        raise DeserializationError("UpdateIPSetRequest.updates required")
    return out
