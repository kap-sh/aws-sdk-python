"""Generated from Smithy shape ``com.amazonaws.kms#DeleteAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kms.types.alias_name_type


class DeleteAliasRequest(TypedDict):
    alias_name: "aws_sdk_kms.types.alias_name_type.AliasNameType"
    """<p>The alias to be deleted. The alias name must begin with <code>alias/</code> followed by the alias name, such as <code>alias/ExampleAlias</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAliasRequest) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAliasRequest:
    out: DeleteAliasRequest = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("DeleteAliasRequest.alias_name required")
    return out
