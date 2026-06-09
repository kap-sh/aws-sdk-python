"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateConnectionStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.terminate_connection_status

TerminateConnectionStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.terminate_connection_status.TerminateConnectionStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateConnectionStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.terminate_connection_status

        aws_sdk_ec2.types.terminate_connection_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TerminateConnectionStatusSet:
    import aws_sdk_ec2.types.terminate_connection_status

    out: TerminateConnectionStatusSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.terminate_connection_status.deserialize_ec2_query(child)
        )
    return out
