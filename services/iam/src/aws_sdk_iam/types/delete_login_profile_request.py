"""Generated from Smithy shape ``com.amazonaws.iam#DeleteLoginProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.user_name_type


class DeleteLoginProfileRequest(TypedDict):
    user_name: NotRequired["aws_sdk_iam.types.user_name_type.userNameType"]
    r"""<p>The name of the user whose password you want to delete.</p> <p>This parameter is optional. If no user name is included, it defaults to the principal making the request. When you make this request with root user credentials, you must use an <a href=\"https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html\">AssumeRoot</a> session to omit the user name.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLoginProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> DeleteLoginProfileRequest:
    out: DeleteLoginProfileRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    return out
