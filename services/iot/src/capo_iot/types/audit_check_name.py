"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckName``."""

from typing import TypeAlias

"""<p>An audit check name. Checks must be enabled for your account. (Use <code>DescribeAccountAuditConfiguration</code> to see the list of all checks, including those that are enabled or use <code>UpdateAccountAuditConfiguration</code> to select which checks are enabled.)</p>"""
AuditCheckName: TypeAlias = str
