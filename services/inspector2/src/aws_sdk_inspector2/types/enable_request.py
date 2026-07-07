"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id_set
    import aws_sdk_inspector2.types.client_token
    import aws_sdk_inspector2.types.enable_resource_type_list


class EnableRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_inspector2.types.account_id_set.AccountIdSet"]
    """<p>A list of account IDs you want to enable Amazon Inspector scans for.</p>"""
    resource_types: (
        "aws_sdk_inspector2.types.enable_resource_type_list.EnableResourceTypeList"
    )
    """<p>The resource scan types you want to enable.</p>"""
    client_token: NotRequired["aws_sdk_inspector2.types.client_token.ClientToken"]
    """<p>The idempotency token for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_inspector2.types.account_id_set

        out["accountIds"] = aws_sdk_inspector2.types.account_id_set.serialize_json(
            value["account_ids"]
        )
    import aws_sdk_inspector2.types.enable_resource_type_list

    out["resourceTypes"] = (
        aws_sdk_inspector2.types.enable_resource_type_list.serialize_json(
            value["resource_types"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> EnableRequest:
    out: EnableRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.account_id_set

        out["account_ids"] = aws_sdk_inspector2.types.account_id_set.deserialize_json(
            data["accountIds"]
        )
    if "resourceTypes" in data:
        import aws_sdk_inspector2.types.enable_resource_type_list

        out["resource_types"] = (
            aws_sdk_inspector2.types.enable_resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    else:
        raise DeserializationError("EnableRequest.resource_types required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
