"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_session


class CreateTrafficMirrorSessionResult(TypedDict):
    traffic_mirror_session: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session.TrafficMirrorSession"
    ]
    """<p>Information about the Traffic Mirror session.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTrafficMirrorSessionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_session" in value:
        import aws_sdk_ec2.types.traffic_mirror_session

        aws_sdk_ec2.types.traffic_mirror_session.serialize_ec2_query(
            value["traffic_mirror_session"], pairs, f"{prefix}.TrafficMirrorSession"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateTrafficMirrorSessionResult:
    out: CreateTrafficMirrorSessionResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_session = el.find("TrafficMirrorSession")
    if child_traffic_mirror_session is not None:
        import aws_sdk_ec2.types.traffic_mirror_session

        out["traffic_mirror_session"] = (
            aws_sdk_ec2.types.traffic_mirror_session.deserialize_ec2_query(
                child_traffic_mirror_session
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
