"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalTableWitnessGroupMemberAction``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class CreateGlobalTableWitnessGroupMemberAction(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Amazon Web Services Region name to be added as a witness Region for the MRSC global table. The witness must be in a different Region than the replicas and within the same Region set:</p> <ul> <li> <p>US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)</p> </li> <li> <p>EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt)</p> </li> <li> <p>AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka)</p> </li> </ul>"""
