"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#MasterUserOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.arn
    import capo_elasticsearch_service.types.password
    import capo_elasticsearch_service.types.username


class MasterUserOptions(TypedDict, closed=True):
    master_user_arn: NotRequired["capo_elasticsearch_service.types.arn.ARN"]
    """<p>ARN for the master user (if IAM is enabled).</p>"""
    master_user_name: NotRequired["capo_elasticsearch_service.types.username.Username"]
    """<p>The master user's username, which is stored in the Amazon Elasticsearch Service domain's internal database.</p>"""
    master_user_password: NotRequired[
        "capo_elasticsearch_service.types.password.Password"
    ]
    """<p>The master user's password, which is stored in the Amazon Elasticsearch Service domain's internal database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MasterUserOptions) -> dict:
    out: dict = {}
    if "master_user_arn" in value:
        out["MasterUserARN"] = value["master_user_arn"]
    if "master_user_name" in value:
        out["MasterUserName"] = value["master_user_name"]
    if "master_user_password" in value:
        out["MasterUserPassword"] = value["master_user_password"]
    return out


def deserialize_json(data: dict) -> MasterUserOptions:
    out: MasterUserOptions = {}  # type: ignore[typeddict-item]
    if "MasterUserARN" in data:
        out["master_user_arn"] = data["MasterUserARN"]
    if "MasterUserName" in data:
        out["master_user_name"] = data["MasterUserName"]
    if "MasterUserPassword" in data:
        out["master_user_password"] = data["MasterUserPassword"]
    return out
