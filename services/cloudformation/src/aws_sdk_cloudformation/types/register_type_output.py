"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegisterTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.registration_token


class RegisterTypeOutput(TypedDict, closed=True):
    registration_token: NotRequired[
        "aws_sdk_cloudformation.types.registration_token.RegistrationToken"
    ]
    """<p>The identifier for this registration request.</p> <p>Use this registration token when calling <a>DescribeTypeRegistration</a>, which returns information about the status and IDs of the extension registration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "registration_token" in value:
        pairs.append((f"{prefix}.RegistrationToken", str(value["registration_token"])))


def deserialize_query(el: Element) -> RegisterTypeOutput:
    out: RegisterTypeOutput = {}  # type: ignore[typeddict-item]
    child_registration_token = el.find("RegistrationToken")
    if child_registration_token is not None:
        out["registration_token"] = str(child_registration_token.text or "")
    return out
