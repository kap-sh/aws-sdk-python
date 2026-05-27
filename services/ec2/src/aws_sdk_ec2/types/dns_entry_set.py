"""Generated from Smithy shape ``com.amazonaws.ec2#DnsEntrySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_entry

DnsEntrySet: TypeAlias = list["aws_sdk_ec2.types.dns_entry.DnsEntry"]
